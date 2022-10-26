# Certificats-cryptography

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
