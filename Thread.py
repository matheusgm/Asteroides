from threading import Thread

class makeThread (Thread):
      ## Constructor.
      #
      #  @param func function to be executed in this thread.
      #
      def __init__ (self,func):
          Thread.__init__(self)
          self.__action = func
          self.debug = False

      ## Obejct destructor.
      #  In Python, destructors are needed much less, because Python has
      #  a garbage collector that handles memory management.
      #  However, there are other resources to be dealt with, such as:
      #  sockets and database connections to be closed,
      #  files, buffers and caches to be flushed.
      #
      def __del__ (self):
          if ( self.debug ): print ("Thread end")

      ## Method representing the thread's activity.
      #  This method may be overriden in a subclass.
      #
      def run (self):
          if ( self.debug ): print ("Thread begin")
          self.__action()
