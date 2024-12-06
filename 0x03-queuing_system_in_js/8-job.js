import redis from 'redis';
import kue from 'kue';

export default function ncreatePushNotificationJobs(jobs, queue) {
  if (!(Array.isArray(jobs))) {
    throw new Error('Jobs is not an array');
  }
  for (const newJob of jobs) {
    const job = queue.create('push_notification_code_3', newJob)
    .save((err) => {
      if (!err) {
        console.log(`Notification job created: ${job.id}`);
      }
    });
    job.on('complete', () => {
      console.log(`Notitfication job ${job.id} completed`);
    });
    job.on('failed', (err) => {
      console.log(`Notification jon ${job.id} failed: ${err}`);
    });
    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  }
}
