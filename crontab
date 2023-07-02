# edit crontab
crontab -e


# ┌───────────── minute (0 - 59)
# │ ┌───────────── hour (0 - 23)
# │ │ ┌───────────── day of the month (1 - 31)
# │ │ │ ┌───────────── month (1 - 12)
# │ │ │ │ ┌───────────── day of the week (0 - 6) (Sunday to Saturday;
# │ │ │ │ │                                   7 is also Sunday on some systems)
# │ │ │ │ │
# │ │ │ │ │
# * * * * * <command to execute>

For example, the following clears the Apache error log at one minute past midnight (00:01) every day, assuming that the default shell for the cron user is Bourne shell compliant:
1 0 * * * printf "" > /var/log/apache/error_log
This example runs a shell program called export_dump.sh at 23:45 (11:45 PM) every Saturday.
45 23 * * 6 /home/oracle/scripts/export_dump.sh
