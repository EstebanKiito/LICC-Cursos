const PromisesSemaphore = require('../src/promises_semaphore');
const Thread = require('../src/thread');

function getThreadList(length, task) {
  return Array.from(
    {length: length, },
    (_, i) => new Thread(i, task)
  );
}

function getStartedPromises(threads) {
  return threads.map(thread => thread.start());
}

describe('Thread Synchronization with Semaphores', () => {
  describe('No Race Conditions in Critical Section', () => {
    it('should protect shared resource', async () => {
      let sharedResource = 0;
      const semaphore = new PromisesSemaphore(1);
      const threadCount = 5;
      const increments = 100;

      const incrementWithLock = async () => {
        for (let i = 0; i < increments; i++) {
          await semaphore.wait();
          sharedResource++;
          semaphore.signal();
        }
      };

      const threads = getThreadList(threadCount, incrementWithLock);

      await Promise.all(getStartedPromises(threads));
      expect(sharedResource).toBe(threadCount * increments);
    });

    it('should run threads once resolved', async () => {
      const semaphore = new PromisesSemaphore(1);
      const threadCount = 3;

      let callback = null;
      const promise = new Promise(resolve => callback = resolve);

      async function task() {
        await semaphore.wait();
        await promise;
        semaphore.signal();
      }

      const threads = getThreadList(threadCount, task);
      const promises = getStartedPromises(threads);
      
      for (const thread of threads) {
        expect(thread.isRunning).toBe(true);
      }
      expect(semaphore.getCount()).toBe(0);
      
      callback();

      await Promise.all(promises);

      for (const thread of threads) {
        expect(thread.isRunning).toBe(false);
      }
      expect(semaphore.getCount()).toBe(1);
    });

    it('should run threads once signaled', async () => {
      const semaphore = new PromisesSemaphore(1);
      await semaphore.wait();
      const threadCount = 3;

      async function task() {
        await semaphore.wait();
        semaphore.signal();
      }

      const threads = getThreadList(threadCount, task);
      const promises = getStartedPromises(threads);

      expect(semaphore.getCount()).toBe(0);
      
      semaphore.signal();

      await Promise.all(promises);

      for (const thread of threads) {
        expect(thread.isRunning).toBe(false);
      }
      expect(semaphore.getCount()).toBe(1);
    });

    it('should block threads', async () => {
      const semaphore = new PromisesSemaphore(1);
      await semaphore.wait();

      async function task() {
        await semaphore.wait();
      }

      const threads = getThreadList(2, task);
      const [thread1, thread2] = threads;
      const promises = getStartedPromises(threads);
      
      semaphore.signal();
      expect(semaphore.getCount()).toBe(0);

      await promises[0];
      
      expect(thread1.isRunning).toBe(false);
      expect(thread2.isRunning).toBe(true);

      semaphore.signal();
      expect(semaphore.getCount()).toBe(0);

      await promises[1];

      expect(thread1.isRunning).toBe(false);
      expect(thread2.isRunning).toBe(false);
    });

    it('should enforce mutual exclusion', async () => {
      const semaphore = new PromisesSemaphore(1);
      const threadCount = 10;
      let maxConcurrent = 0;
      let currentConcurrent = 0;

      const criticalSection = async () => {
        await semaphore.wait();
        currentConcurrent++;
        maxConcurrent = Math.max(maxConcurrent, currentConcurrent);
        currentConcurrent--;
        semaphore.signal();
      };

      const threads = getThreadList(threadCount, criticalSection);

      await Promise.all(getStartedPromises(threads));
      expect(maxConcurrent).toBe(1);
    });
  });

  describe('Producer-Consumer Synchronization', () => {
    it('should synchronize producer and consumer without data loss', async () => {
      const buffer = [];
      const bufferSize = 2;
      const emptySlots = new PromisesSemaphore(bufferSize);
      const fullSlots = new PromisesSemaphore(bufferSize);
      for (let i = 0; i < bufferSize; i++) 
        await fullSlots.wait();
      
      const mutex = new PromisesSemaphore(1);

      let produced = 0;
      let consumed = 0;

      const producer = async () => {
        for (let i = 0; i < 5; i++) {
          await emptySlots.wait();
          await mutex.wait();
          buffer.push(i);
          produced++;
          mutex.signal();
          fullSlots.signal();
        }
      };

      const consumer = async () => {
        for (let i = 0; i < 5; i++) {
          await fullSlots.wait();
          await mutex.wait();
          buffer.shift();
          consumed++;
          mutex.signal();
          emptySlots.signal();
        }
      };

      const producerThread = new Thread(1, producer);
      const consumerThread = new Thread(2, consumer);

      await Promise.all([producerThread.start(), consumerThread.start()]);

      expect(produced).toBe(5);
      expect(consumed).toBe(5);
      expect(buffer).toHaveLength(0);
    });

    it('should prevent buffer overflow', async () => {
      const buffer = [];
      const bufferSize = 1;
      const emptySlots = new PromisesSemaphore(bufferSize);
      const mutex = new PromisesSemaphore(1);

      const producer = async () => {
        for (let i = 0; i < 5; i++) {
          await emptySlots.wait();
          await mutex.wait();
          buffer.push(i);
          mutex.signal();
          expect(buffer.length).toBeLessThanOrEqual(bufferSize);
        }
      };

      const thread = new Thread(1, producer);
      thread.start();
      expect(buffer.length).toBeLessThanOrEqual(bufferSize);
      expect(thread.isRunning).toBe(true);
    });
  });
});