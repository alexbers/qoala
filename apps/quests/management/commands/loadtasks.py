from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from quests.models import Quest
import os
from os.path import basename

__author__ = 'Last G'


class Command(BaseCommand):
    can_import_settings = True

    def load_task(self, shortname, checker_path, checker_type):
        if Quest.objects.filter(provider_file=checker_path).exists():
            quest = Quest.objects.filter(provider_file=checker_path).get()
        else:
            quest = Quest(shortname=shortname)

        quest.provider_file = checker_path
        quest.provider_type = checker_type
        quest.update_from_file(checker_type, checker_path)
        quest.save()

    def find_task(self, folder):
        pre_short = basename(folder).lower()
        for f in os.listdir(folder):
            checker_path = os.path.abspath(os.path.join(folder, f))
            fname = basename(f.lower())
            if os.path.isfile(checker_path):
                if fname == pre_short + ".xml":
                    return pre_short, checker_path, 'XMLQuestProvider'
                elif fname == pre_short:
                    return pre_short, checker_path, 'ScriptQuestProvider'

    def handle(self, *args, **options):
        for taskdir in os.listdir(settings.TASKS_DIR):
            path = os.path.join(settings.TASKS_DIR, taskdir)
            if os.path.isdir(path):
                print("Checking {} for task".format(path))
                res = self.find_task(path)
                if res:
                    shortname, checker, provider = res
                    print("Loading task {} from {}".format(shortname, checker))
                    self.load_task(shortname, checker, provider)
