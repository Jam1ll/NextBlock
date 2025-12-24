import axios from 'axios';

const instance = axios.create({
  baseURL: "/api", 
  timeout: 50000,
  headers: {
    'Content-Type': 'application/json',
  }
});

export default instance;