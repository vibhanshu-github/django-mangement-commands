from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('app', nargs='?', type=str)

    def handle(self, *args, **options):
        if(not options['app']):
            raise CommandError("no app found!" % app)
        else:
            app = options['app']
        from django.core.management import call_command
        call_command("startapp",options['app'], interactive=True)

        import os
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        FILE_PATH = os.path.join(BASE_DIR,os.path.split(BASE_DIR)[-1],'settings.py')
        with open(FILE_PATH, "r") as f:
            contents = f.readlines()

        for i,line in enumerate(contents):
            if("INSTALLED_APPS" in line):
                self.stdout.write("{i}->{line}".format(i=i,line=line))
                for j,l in enumerate(contents[i:]):
                    if("]" in l):
                        self.stdout.write("{i}->{line}:length={length}".format(i=i+j,line=l,length=len(l)))
                        app_path = os.path.join(BASE_DIR,app)
                        if os.path.isdir(app_path) is True:
                            self.stdout.write(app_path)
                            """ Code to create static folder hierarichy """
                            os.makedirs(os.path.join(app_path,"static",app),exist_ok=True)
                            os.makedirs(os.path.join(app_path,"static",app,"css"),exist_ok=True)
                            os.makedirs(os.path.join(app_path,"static",app,"css","fonts"),exist_ok=True)
                            os.makedirs(os.path.join(app_path,"static",app,"js"),exist_ok=True)
                            os.makedirs(os.path.join(app_path,"static",app,"img"),exist_ok=True)
                            """ Code to create templates folder """
                            os.makedirs(os.path.join(app_path,"templates",app),exist_ok=True)
                        else:
                            raise CommandError("'%s' app does not exist" % app)
                        app = "    '"+app+"',\n"
                        contents.insert(i+j,app)
                        with open(FILE_PATH, "w") as fo:
                            fo.write("".join(contents))
                        return
