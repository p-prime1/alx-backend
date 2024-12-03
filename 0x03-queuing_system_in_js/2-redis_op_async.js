import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
client.on('connect', () => {
  console.log('Redis client is connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

const set = promisify(client.set).bind(client);
const get = promisify(client.get).bind(client);

async function setNewSchool(schoolName, value) {
  const reply = await set(schoolName, value)
  console.log(reply);
}

async function displaySchoolValue(schoolName) {
  try {
    const reply = await get(schoolName);
    console.log(reply);
  } catch (err) {
    console.error(err);
  }
}

(async () => {
  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
})();
