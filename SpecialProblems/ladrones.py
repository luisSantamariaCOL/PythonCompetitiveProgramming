'''
Problema inventado por Luis Santamaría.
En un país la corrupción está al tope, las instituciones y el gobierno tienen mala imagen
y la justicia está cada vez más parcializada a favor de los corruptos.
Gobernadores y alcaldes roban mucho. Se reciben denuncias sobre ellos pero nunca los ponen presos.
Los ciudadanos empiezan a hacer presión, así que los organos de la rama judicial, para mantener la
poca buena imagen que tienen, deciden crear las siguientes reglas:
    - Si al político se le llega a pillar 5 veces robando, se le da casa por cárcel 5 años.
    - Si la suma de lo que se ha robado un político, es mayor a los 12 mil millones de peso, se le da
    casa por cárcel 5 años.
    - Si la ciudadanía y los medios (independientes, obvio), hacen presión al menos 3 veces, al político se le
    abre un proceso investigativo que le de al final casa por cárcel 5 años.

Imprima en pantalla el momento en el que un político corrupto deba pagar casa por carcel.
'''
def main():
    bd_corruptos = {}
    while True:
        corrupto = input("Ingrese el nombre de algún político pillado en un acto de corrupción: ").casefold()
        if corrupto not in bd_corruptos:
            bd_corruptos[corrupto] = 1
        else:
            bd_corruptos[corrupto] += 1
            if bd_corruptos[corrupto] == 5:
                print("El político {} tiene que pagar 5 años de casa por cárcel".format(corrupto))
                bd_corruptos[corrupto] = 0
        print(bd_corruptos)
if __name__ == '__main__':
    main()