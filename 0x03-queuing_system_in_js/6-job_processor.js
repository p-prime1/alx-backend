import redis from 'redis';
import kue from 'kue';

const queue = kue.createQueue();

const data = {
  phoneNumber: 9399939,
  message: 'Notice',
};

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

const job = queue.create('Notification', data).save();

queue.process('Notification', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});
