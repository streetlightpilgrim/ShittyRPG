import django, os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shitty_rpg.settings")
django.setup()

from game.models import Item
from Character import run

print('Here are all the items:')
print([item.name for item in Item.objects.all()])

run()
