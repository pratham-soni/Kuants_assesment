const filterByFrequency = (clients)=>{
    const companies_frequency = new Map();
    let total = 0;
    for(const client of clients){
        if(!companies_frequency.has(client)){
            companies_frequency.set(client, 1);
        }else{
            companies_frequency.set(client, companies_frequency.get(client)+1);
        }
        total++;
    }
    let result = new Array();
    for(const [company_name, value] of companies_frequency){
        let percentage = (value/total)*100;
        if(percentage >= 7){
            result.push(company_name);
        }
    }
    result.sort();
    return result;
}

console.log(filterByFrequency(["Bigcorp","Bigcorp","Acme","Bigcorp","Zork","Zork","Abc","Bigcorp",
"Acme","Bigcorp","Bigcorp","Zork","Bigcorp","Zork","Zork","Bigcorp","Acme",
"Bigcorp","Acme","Bigcorp","Acme","Littlecorp","Nadircorp"]))