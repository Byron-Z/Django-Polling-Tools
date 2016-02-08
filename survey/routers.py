class TOMRouter(object):
    """
    A router to control all database operations on models in
    the Polls application
    """
 
    def db_for_read(self, model, **hints):
        """
        Point all operations on tom models to 'tom'
        """
        if model._meta.app_label == 'tom':
            return 'tom'
        return None
 
    def db_for_write(self, model, **hints):
        """
        Point all operations on myapp models to 'other'
        """
        if model._meta.app_label == 'tom':
            return 'tom'
        return None
 
    def allow_syncdb(self, db, model):
        """
        Make sure the 'tom' app only appears on the 'other' db
        """
        if db == 'tom':
            return model._meta.app_label == 'tom'
        elif model._meta.app_label == 'tom':
            return False
        return None