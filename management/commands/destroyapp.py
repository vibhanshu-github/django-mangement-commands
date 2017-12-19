from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('app', nargs='?', type=str)

    def handle(self, *args, **options):
        if(not options['app']):
            raise CommandError("no app found!" % app)
        else:
            app = options['app']

        import os
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        FILE_PATH = os.path.join(BASE_DIR,BASE_DIR.split('/')[-1]+'/settings.py')
        with open(FILE_PATH, "r") as f:
            contents = f.readlines()

        for i,line in enumerate(contents):
            if("INSTALLED_APPS" in line):
                for j,l in enumerate(contents[i:]):
                    if(app in l):
                        self.stdout.write("{i}->{line}:length={length}".format(i=i+j,line=l,length=len(l)))
                        app_path = os.path.join(BASE_DIR,app)
                        if os.path.isdir(app_path) is True:
                            self.stdout.write(app_path)
                            import shutil
                            shutil.rmtree(app_path)
                        else:
                            del contents[i+j]
                            with open(FILE_PATH, "w") as fo:
                                fo.write("".join(contents))
                            raise CommandError("'%s' app does not exist" % app)
                        
                        del contents[i+j]
                        with open(FILE_PATH, "w") as fo:
                            fo.write("".join(contents))
                        return
