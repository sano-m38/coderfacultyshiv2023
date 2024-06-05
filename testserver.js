// example got from blackbox

// var http = require('http');

// Create a server object
const server = http.createServer((req, res) => {
  // Set the response header
res.writeHead(200, { 'Content-Type': 'text/plain' });

  // Send the response body
res.end('sup, World!');
});

// Start the server on port 3000
server.listen(5000, 'localhost', () => {
console.log('Server running at http://localhost:3000/');
});

// not working when writing cd testserver.js via terminal it say does not exist. 
// even when writing node testserver.js nothing happen or even the URL http://localhost:3000/ ?       found the solution there was other application running on the port 3000 only one can run 
// to make it run type node testserver.js
// problem happen again , stoped port then relunched using node testserver.js which show node:events:492 throw error



// example got from note
const http = require('http');

// Create a server instance
const server = http.createServer((req, res) => {
res.writeHead(200, { 'Content-Type': 'text/plain' });
res.end('Hello world!');
});

// Listen on a specific port
const port = 3000;
server.listen(port, () => {
console.log(`Server is listening on port ${port}`);
});
// this one is showingthe same probleme









