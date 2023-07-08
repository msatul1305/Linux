# e.g. to decide partition key
    - must be unique
    - must be equally partitioned
    - must never not change the value(e.g. empid)
{
empid: '5fg45f',
name: 'aia',
email: 'aa@gg.com',
office: 'UST1',
department: 'dev',
reportsto: ''
}

email id: could change
office: not evenly distributed(HOT partition)
department: not evenly distributed and could change
empid: is unique and can be used as parition key 
