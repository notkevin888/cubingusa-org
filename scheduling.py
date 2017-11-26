import webapp2

from src import config
from src.handlers.scheduling.index import SchedulingIndexHandler
from src.handlers.scheduling.edit_competition import EditCompetitionHandler
from src.handlers.scheduling.edit_schedule import EditScheduleHandler
from src.handlers.scheduling.new_competition import NewCompetitionHandler
from src.handlers.scheduling.new_schedule import NewScheduleHandler
from src.handlers.scheduling.set_live import SetLiveHandler

app = webapp2.WSGIApplication([
  webapp2.Route('/scheduling', handler=SchedulingIndexHandler, name='index'),
  webapp2.Route('/scheduling/edit/<competition_id:.*>',
                handler=EditCompetitionHandler,
                name='edit_competition'),
  webapp2.Route('/scheduling/new_competition',
                handler=NewCompetitionHandler,
                name='new_competition'),
  webapp2.Route('/scheduling/edit_schedule/<schedule_version:.*>',
                handler=EditScheduleHandler,
                name='edit_schedule'),
  webapp2.Route('/scheduling/new_schedule/<competition_id:.*>',
                handler=NewScheduleHandler,
                name='new_schedule'),
  webapp2.Route('/scheduling/set_live/<schedule_version:.*>/<set_live:\d>',
                handler=SetLiveHandler,
                name='set_live'),
], config=config.GetAppConfig())
