# PASOS PARA INSTALAR ELEMENTOS DEL CURSO MAC M1!!!

```
brew install gnupg2
gpg --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
curl -sSL https://get.rvm.io | bash -s stable
```

Utilizar Rosetta en caso de errores.

`brew install postgresql`

rvm install ruby-3.1.0 --reconfigure --enable-yjit --with-openssl-dir=$(brew --prefix openssl@3)

```
gem install rails -v 7.0.4
`brew services start postgresql`
```

```
rails new nombre-proyecto --database=postgresql
cd nombre-proyecto
bundle install
```
