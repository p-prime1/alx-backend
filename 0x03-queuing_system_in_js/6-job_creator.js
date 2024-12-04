import redis from 'redis';
import kue from 'kue';

const data = {
  phoneNumber: '01010',
  message: 'complete',
}

const client = redis.createClient();
const queue = kue.createQueue();

const job = queue.create('Notification').save((err) => {
  if (err) {
    console.log(`Notification job failed`);
  } else {
    console.log(`Notification job created: ${job.id}`);
    console.log('Notification job completed');
  }
});
