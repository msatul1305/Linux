// here, "order" is used from "queueTrigger" defined in functions.json file
module.exports = function (context, order){
    order.PartitionKey = "Orders";
    order.RowKey = generateRandomId();

    context.done(null, order);
};

function generateRandomId(){
    return Math.random().toString(36).substring(2, 15) +
            Math.random().toString(36).substring(2, 15);
}
