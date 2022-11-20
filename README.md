# RSA Simulation

This is a school project I made with Crispel Clement. The goal is to generate a simuation, of 1 person sending is public key to an other, with a certificat.  
All the code is in python.

## The code will automatically make the scenario

  // Alice : tire 2 nombres premiers pA et qA, nA=pA*qA
  // Alice : clé publique (eA,nA)
  // Alice : clé privée (dA,nA)

  // CA : tire 2 nombres premiers pCA et qCA, nCA=pCA*qCA
  // CA : clé publique (eCA,nCA)
  // CA : clé privée (dCA,nCA)

  // Alice : construire un message contenant sa clé publique et son empreinte
  // (elle signe en chiffrant l'empreinte avec sa clé privée)
  // (elle communique de manière confidentielle avec CA, en chiffrant avec la clé publique de CA)

  // CA : récupère la clé publique d'Alice et vérifie l'empreinte
  // CA : génère le certificat de la clé publique d'Alice
  // (chiffrement de la clé publique d'Alice avec la clé privée de CA)

  // Bob : vérifie le certificat d'Alice
  // (la clé publique d'Alice doit correspondre au déchiffrement du certificat avec la clé publique de CA)


## Tests
There is asserts in my code to test and stop the code if there is an issue
## Trick I use
All the message I send are list.  
I put at the beggining of the message ( list ) the len of the first part of the key.  
The hash function will always return an hash of len 4.

<i>Made by CRISPEL Clement and FOURCAUDOT Tom </i>  
20 Novemeber 2022