The basic classes are

    Loggers expose the interface that application code directly uses.
        * logging.getLogger()

    Handlers send the log records (created by loggers) to the appropriate destination.
      * Stream, File, TCP/IP, UDP, SMTP (email), SysLog (unix daemon), HTTP

    Filters provide a finer grained facility for determining which log records to output.

    Formatters specify the layout of log records in the final output.

logger hierarchy: denoted by period-separation - emb.mike, emb.fred, emb.nat, emb.seb are all descendants of emb
  * root is ultimate parent. Breaks this rule (ie root is parent to emb)

basicConfig - creates a StreamHandler with default Formatter and adds it to the root logger at warning level
  * note, this is called automatically by the root logger if not otherwise configured

level - loggers use their parent's level if not otherwise configured

logging.lastResort - internal handler not associated with any logger. StreamHandler to stderr, set to WARNING

Interesting:  
https://github.com/madzak/python-json-logger