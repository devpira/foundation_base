const { ApolloServer, gql } = require('apollo-server');
var PROTO_PATH = __dirname + '/grpc/proto/user.proto';
var grpc = require('grpc');
var protoLoader = require('@grpc/proto-loader');

var packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true
    });

var userDescriptor = grpc.loadPackageDefinition(packageDefinition).user.grpc;
var client = new userDescriptor.User('192.168.99.100:8000', grpc.credentials.createInsecure());

const dataSource = [
    {
        id: 1,
        first_name: "pira",
        last_name: "man",
        email: "pira@gmail.com",
        gender: "male",
    },
    {
        id: 2,
        first_name: "Man",
        last_name: "Pira",
        email: "ManPira@gmail.com",
        gender: "female",
    },
];

const typeDefs = gql`
  # Comments in GraphQL strings (such as this one) start with the hash (#) symbol.

  # This "Book" type defines the queryable fields for every book in our data source.
  type User {
    id: Int
    first_name: String
    last_name: String
    email: String
    gender: String
  }

  # The "Query" type is special: it lists all of the available queries that
  # clients can execute, along with the return type for each. In this
  # case, the "books" query returns an array of zero or more Books (defined above).
  type Query {
    users: [User]
    user(id: Int): User
  }

  type Mutation {
    createUser(first_name: String, last_name: String, email: String, gender: String): User
  }   
`;

const resolvers = {
    Query: {
        users: (parent, args, context) => {
            return dataSource
        },
        user: (parent, { id }, context) => dataSource.filter((item) => item.id === id)[0],
    },
    Mutation: {
        async createUser(_, { first_name, last_name, email, gender }) {
            const request = {
                // id: 15,
                first_name: first_name,
                last_name: last_name,
                email: email,
                gender: gender,
            };
            
            let returnResult = {}

            var createUserRequest = (args) => {
                return new Promise((returnValue, returnErrorValue) => {
                    client.createUser(args, function (err, response) {
                        if (response.result) {
                            console.log('Result:', response.result);
                            returnValue(response.result)
                        } else if (err) {
                            returnErrorValue(err)
                        }
                    });
                });
            }

            await createUserRequest(request).then(
                result => {
                    returnResult = result
                }
            ).catch(
                error => console.log(error)
            )

            return JSON.parse(returnResult)
        }
    }
};

const server = new ApolloServer({ typeDefs, resolvers });

// The `listen` method launches a web server.
server.listen().then(({ url }) => {
    console.log(`🚀  Server ready at ${url}`);
});