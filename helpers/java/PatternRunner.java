import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.regex.Pattern;

/** Tiny ground-truth runner for the JDK's java.util.regex.Pattern engine. */
public final class PatternRunner {
  private static String javaVersion() {
    return System.getProperty("java.vendor") + " " + Runtime.version().toString();
  }

  private static String json(String value) {
    StringBuilder escaped = new StringBuilder("\"");
    for (int i = 0; i < value.length(); i++) {
      char ch = value.charAt(i);
      switch (ch) {
        case '"': escaped.append("\\\""); break;
        case '\\': escaped.append("\\\\"); break;
        case '\b': escaped.append("\\b"); break;
        case '\f': escaped.append("\\f"); break;
        case '\n': escaped.append("\\n"); break;
        case '\r': escaped.append("\\r"); break;
        case '\t': escaped.append("\\t"); break;
        default:
          if (ch < 0x20) {
            escaped.append(String.format("\\u%04x", (int) ch));
          } else {
            escaped.append(ch);
          }
      }
    }
    return escaped.append('"').toString();
  }

  private static int patternFlags(String flags) {
    int result = 0;
    for (int i = 0; i < flags.length(); i++) {
      switch (flags.charAt(i)) {
        case 'i': result |= Pattern.CASE_INSENSITIVE; break;
        default: throw new IllegalArgumentException("unsupported flag: " + flags.charAt(i));
      }
    }
    return result;
  }

  public static void main(String[] args) throws IOException {
    if (args.length < 2 || args.length > 4) {
      System.err.println("usage: PatternRunner parse|match PATTERN [FLAGS] [CALL_KIND]");
      System.exit(2);
    }
    String mode = args[0];
    String expression = args[1];
    String flags = args.length >= 3 ? args[2] : "";
    String callKind = args.length >= 4 ? args[3] : "search";
    final Pattern compiled;
    try {
      compiled = Pattern.compile(expression, patternFlags(flags));
    } catch (IllegalArgumentException error) {
      System.out.println("{\"ok\":false,\"unencodable_reason\":\"parse-error\",\"error\":"
          + json(error.getMessage() == null ? "invalid pattern" : error.getMessage())
          + ",\"helper\":\"java-pattern\",\"version\":"
          + json(javaVersion()) + "}");
      System.exit("parse".equals(mode) ? 1 : 2);
      return;
    }
    if ("parse".equals(mode)) {
      System.out.println("{\"ok\":true,\"helper\":\"java-pattern\",\"version\":"
          + json(javaVersion()) + "}");
      return;
    }
    if (!"match".equals(mode)) {
      System.err.println("unknown mode: " + mode);
      System.exit(2);
    }
    String input = new String(System.in.readAllBytes(), StandardCharsets.UTF_8);
    var matcher = compiled.matcher(input);
    boolean matched;
    switch (callKind) {
      case "fullmatch": matched = matcher.matches(); break;
      case "match": matched = matcher.lookingAt(); break;
      case "search": case "exec": case "substitution": matched = matcher.find(); break;
      default:
        System.err.println("unsupported call kind: " + callKind);
        System.exit(2);
        return;
    }
    System.out.println("{\"ok\":true,\"matched\":" + matched
        + ",\"helper\":\"java-pattern\",\"version\":"
        + json(javaVersion()) + "}");
    System.exit(matched ? 0 : 1);
  }
}
