var express = require('express');
var { graphqlHTTP } = require('express-graphql');
var { buildSchema } = require('graphql');
 
var schema = buildSchema(`

  type Student {
    studentid: String
    studentname: String
    studentdob: String
 }
 
  type Query {
   
    studentQueryById(studentid: String): Student
    studentQueryByName(studentname : String): Student
    studentQueryByDob(studentdob : String): Student
    othercall: String
  }
`);
 
var studentDatabase = {
    'a': {
    studentid: 'b0001',
    studentname: 'alice',
    studentdob: '1999'
  },
  'b': {
    studentid: 'b0002',
    studentname: 'bob',
    studentdob: '1998'
  },
  'c': {
    studentid: 'b0003',
    studentname: 'james',
    studentdob: '1994'
  },
  'd': {
    studentid: 'b0004',
    studentname: 'arka',
    studentdob: '1995'
  },
  'e': {
    studentid: 'b0005',
    studentname: 'alan',
    studentdob: '1996'
  },
};

var root = {
    
  studentQueryById:({studentid}) => {
	  
	  const propOwn = Object.getOwnPropertyNames(studentDatabase);
	  
	  for(let item in studentDatabase){
		  let temp = studentDatabase[item];
		 
			  if(temp.studentid == studentid){
				  return temp;
				
		  }
	  }
      
  },
  studentQueryByName:({studentname}) => {
      //send back the data 
	  
	  const propOwn = Object.getOwnPropertyNames(studentDatabase);
	  
	  for(let item in studentDatabase){
		  let temp = studentDatabase[item];
		 
			  if(temp.studentname == studentname){
				  return temp;
				
		  }
	  }
      
  },
  studentQueryByDob:({studentdob}) => {
      //send back the data 
	  const propOwn = Object.getOwnPropertyNames(studentDatabase);
	  
	  for(let item in studentDatabase){
		  let temp = studentDatabase[item];
		 
			  if(temp.studentdob == studentdob){
				  return temp;
				
		  }
	  }
      
  },
   othercall: ({}) => {
  return 'This is the other call';
  }
};


 
var app = express();
app.use('/graphql', graphqlHTTP({
  schema: schema,
  rootValue: root,
  graphiql: true,
}));
app.listen(4000);
console.log('Running a GraphQL API server at localhost:4000/graphql');