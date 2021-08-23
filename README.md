# Blockchain for record team activities

## Work description
- Implement Blockchain in a network to record computer activities.
- Create a frontend application.

##  and explanation
I used the hashlib library to store each of the blocks inserted in the blockchain system, encrypting them in SHA-256, receiving the requests via HTTP. The received information is linked with the encryption of the previous information. Each block contains the creation date, the number of iterations to validate it (proof of work), and the aggregated information linked to the previous one.
In addition, the blocks are stored in mongodb and in a .txt file on the server's local hard disk.
The frontend of the application was created in ReactJS.

### Technologies
- Python Flask
- MongoDB
- ReactJS

### ENDPOINTS

> #### **POST**
`"/new"`<br>
**REQUIREMENTS**
- JSON
```json
{
    "data" : "The new information",
}
```

> #### **POST**
`"/get"`<br>
**REPONSE**
- JSON (With all the inserted blocks)
```json
[{...}]
```