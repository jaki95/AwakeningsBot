import schedule
import event
import os

chat_id = 1317888738

scrape_interval = os.environ.get('AWK-SCRAPE')

if scrape_interval == 1:
    schedule.every().minute.at(":01").do(event.check_events)
if scrape_interval == 60:
    schedule.every().hour.at(":01").do(event.check_events)

while True:
    schedule.run_pending()
