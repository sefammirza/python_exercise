sales = {
  "cost_value": 31.87,
  "sell_value": 45.00,
  "inventory": 1000
}  

result = (sales["sell_value"]- sales["cost_value"]) * sales["inventory"]
print(round(result))
