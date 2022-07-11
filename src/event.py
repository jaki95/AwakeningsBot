import scrape
import message


def check_events():
    """
    Checks Awakenings event page and sends a message if new events are added

    :return: None
    """

    print("checking events...")
    events = scrape.scrape("https://www.awakenings.com/en/events/", "eventslist-item__title")

    if len(events) > 4:
        print("new events found - notifying")
        message.send_message("New Awakenings event added! \nhttps://www.awakenings.com/en/events/")
    else:
        print("no new events")
