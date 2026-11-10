class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:

        invalid_indices = set()
        list_transactions = []
        results = []

        for i, transaction in enumerate(transactions):
            record = transaction.split(",")
            name = record[0]

            list_transactions.append(record)

            if int(record[2]) > 1000:
                invalid_indices.add(i)
        
        for i in range(len(list_transactions)):
            namei = list_transactions[i][0]
            timei = int(list_transactions[i][1])
            cityi = list_transactions[i][3]

            for j in range(len(list_transactions)):
                namej = list_transactions[j][0]
                timej = int(list_transactions[j][1])
                cityj = list_transactions[j][3]

                if abs(timei - timej) <= 60 and namei == namej and cityi != cityj:
                    invalid_indices.add(i)
        
        for index in invalid_indices:
            results.append(transactions[index])

        return results

        



        




        


        