#!/usr/bin/node

const argC = process.argv.length;

if (argC === 0){
	console.log('No argument');
} else if (argC === 1){
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
