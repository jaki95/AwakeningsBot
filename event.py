import crawl
import message


def check_events():
    print("checking events...")
    events = crawl.crawling("https://www.awakenings.com/en/events/", "eventslist-item__title")
    if len(events) > 4:
        message.send_message("New Awakenings event added! \nhttps://www.awakenings.com/en/events/")
        print("new events found - notifying")
    else:
        print("no new events")
