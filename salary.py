import os
os.system('cls||clear')

# Inputs
payed_per_hour = float(input("Digite o quanto recebe por hora trabalhada: "))
worked_time = input("Digite o tempo trabalhado no mês no formato h:m:s : ")
hour, minute, second = [float(x) for x in worked_time.split(":")]

# Calc
time_to_seconds = hour*3600 + minute*60 + second
result = format(time_to_seconds * (payed_per_hour/3600), '.2f')

# Return
print(
    f"\n------ \n\nO salário a ser pago nesse mês é \n\nR$ {result} \n\n------\n"
)
