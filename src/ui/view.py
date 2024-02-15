import weakref

class ANView(object):

    def __init__(self, root, view_model):
        self._root = weakref.ref(root)
        self._view_model = weakref.ref(view_model)
        
    def load_frames(self):
        pass

    def get_root(self):
        return self._root()
    
    def get_view_model(self):
        return self._view_model()