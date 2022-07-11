import schedule
import event
import yaml

chat_id = 1317888738

with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

if config['scrape_every'] == 1:
    schedule.every().minute.at(":01").do(event.check_events)
if config['scrape_every'] == 60:
    schedule.every().hour.at(":01").do(event.check_events)

while True:
    schedule.run_pending()
