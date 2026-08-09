/* Minimal DOMPurify regexp.ts sample (Wave 3 / #115). */
import { seal } from './utils.js';

export const IS_ALLOWED_URI = seal(
  /^(?:(?:(?:f|ht)tps?|mailto|tel|callto|sms|cid|xmpp|matrix):|[^a-z]|[a-z+.\-]+(?:[^a-z+.\-:]|$))/i
);
export const IS_SCRIPT_OR_DATA = seal(/^(?:\w+script|data):/i);
export const DOCTYPE_NAME = seal(/^html$/i);
