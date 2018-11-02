"""
Synopsis:
    Use 3 (or more) worker threads to process a list of "jobs".
    Place the jobs in a queue (an instance of Queue.Queue).
    Enable the worker threads to process the jobs.
    Here is a list of jobs -- Multiply the first item of each
    tuple by the second:
        JobsInputlist = [
            (5, 5),
            (10, 4),
            (78, 5),
            (87, 2),
            (65, 4),
            (10, 10),
            (65, 2),
            (88, 95),
            (44, 55),
            (33, 3),
        ]
Usage:
    python threads_and_queue.py
Hints:
    - threading module in the Python standard library
    - Queue module in the Python standard library
    - time.sleep() from the time module in the Python standard library
"""

# Adapted from the example at:
#   http://www.boschmans.net/2010/02/03/simple-python-threading-thread-example/
# Thanks to
# Alex Boschmans
# www.boschmans.net


import threading
import Queue
import time


# This is how many threads we want
THREAD_LIMIT = 3
# This is how long we want each thread to delay so as to simulate processing
THREAD_DELAY = 2
# This sets up the queue object to use 5 slots
JobQueue = Queue.Queue(5)
# This is a lock so threads don't print through each other (and other reasons)
SingleLock = threading.Lock()

# Our list of work todo
JobsInputlist = [
    (5, 5),
    (10, 4),
    (78, 5),
    (87, 2),
    (65, 4),
    (10, 10),
    (65, 2),
    (88, 95),
    (44, 55),
    (33, 3),
]


#
# The worker thread class - based on threading.Thread
# This class is cloned/used as a thread template to spawn those threads.
# The class has a run function that gets a job out of the JobQueue queue
# And lets the queue object know when it has finished.
#
class Worker(threading.Thread):
    def __init__(self, workernumber):
        threading.Thread.__init__(self)
        self.workernumber = workernumber

    def run(self):
        # run forever
        while True:
            # Try and get a job out of the queue
            try:
                #
                # Process a job
                job = JobQueue.get(True, 1)
                self.process_a_job(job)
                # End of processing a job.
                #
            except Queue.Empty:
                break           # No more jobs in the queue

    def process_a_job(self, job):
        SingleLock.acquire()        # Acquire the lock
        msg = "Worker {0} -- {1} times {2} --> {3}"
        print msg.format(
            self.workernumber, job[0], job[1], (job[0]*job[1]))
        SingleLock.release()        # Release the lock
        # Let the queue know the job is finished.
        JobQueue.task_done()
        # Delay so as to force other workers to run.
        # This simulates processing/task that takes a long time.
        time.sleep(THREAD_DELAY)


#
# The main function.
# It spawns the threads, fills up the queue with work
# items that the threads will use
# And then waits for the threads to finish.
# This could use some more try:except code...
#
def main():
    print "Inputlist received..."
    print JobsInputlist

    # Spawn the threads
    print "Spawning the {0} threads.".format(THREAD_LIMIT)
    for index in xrange(THREAD_LIMIT):
        print "Thread {0} started.".format(index)
        # This is the thread class that we instantiate.
        worker = Worker(index)
        worker.start()

    # Put stuff in queue
    print "Putting stuff in queue"
    for job in JobsInputlist:
        # Block if queue is full, and wait 5 seconds.
        # After 5 seconds raise Queue Full error.
        try:
            JobQueue.put(job, block=True, timeout=5)
        except Queue.Full:
            SingleLock.acquire()
            # We do not arive here because Queue.put blocks and waits.
            print "The queue is full!"
            SingleLock.release()

    # Wait for the threads to finish.
    SingleLock.acquire()        # Acquire the lock so we can print
    print "Waiting for threads to finish."
    SingleLock.release()        # Release the lock
    # This command waits for all threads to finish.
    JobQueue.join()


if __name__ == '__main__':
    main()
