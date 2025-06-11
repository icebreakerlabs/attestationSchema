const { attestationSchemas } = require('./attestationSchemas');
const fs = require('fs');

fs.writeFileSync('attestationSchemas.json', JSON.stringify(attestationSchemas, null, 2));