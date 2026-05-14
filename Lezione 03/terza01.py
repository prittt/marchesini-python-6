#nome = input("Come ti chiami? ")
#eta = int(input("Quanti anni hai? "))
#altezza = float(input("Quanto sei alto (cm)? "))

nome = 'Costantino'
eta = 50
altezza = 183.0

print("Ti chiami", nome, ", hai", eta, "anni e sei alto", altezza, "cm")

s = ("Ti chiami " + nome + ", hai " + str(eta) + " anni e sei alto " + 
      str(altezza) + " cm")
print(s)

msg_ita = "Ti chiami {0}, hai {1} anni e sei alto {2:.0f} cm"
msg_eng = "Your name is {0} and you are {2:.0f} cm tall and {1} years old"
msg = msg_ita
print(msg.format(nome, eta, altezza))
msg = msg_eng
print(msg.format(nome, eta, altezza))

print(f"Ti chiami {nome.upper()}, hai {eta - 2} anni e sei alto {altezza:.0f} cm")
