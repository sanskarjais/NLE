import os
import play_scraper as ps
import json

# Cron Job
from django_cron import CronJobBase, Schedule


class CallScrapper(CronJobBase):   

    RUN_EVERY_MINS = 60 * 24
    schedule = Schedule(run_every_mins = RUN_EVERY_MINS)
    code = 'android.call_scrapper'

    def do(self):
        a = ps.categories()
        lis = list(a.keys())
        with open('data.json', 'w') as fjson:
            json.dump(lis, fjson)





