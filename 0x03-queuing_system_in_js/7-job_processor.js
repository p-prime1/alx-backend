import kue from 'kue';
import redis from 'redis';

const blackList = ['4153518780', '4153518781'];

const queue = kue.createQueue();

function sendNotification(phoneNumber, message, job, done) {
  const totalSteps = 100;
  let completedSteps = 0;

  if (blackList.includes(phoneNumber)) {
    const error = new Error(`Phone number ${phoneNumber} is 
      blacklisted`);
    return done(error);
  }

  const interval = setInterval(() => {
    completedSteps += 10;
    job.progress(completedSteps, totalSteps);

    if (completedSteps >= 50) {
      clearInterval(interval);
      done();
    }
    console.log(`Sending notification to ${phoneNumber} with message ${
      message}`);
  }, 100);
}

queue.process('push_notification_code_2', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
