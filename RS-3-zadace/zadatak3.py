import asyncio


# 3
async def autentifikacija(korisnicko_ime, email, lozinka):
    for korisnik in baza_korisnika:
        if korisnik["korisnicko_ime"] == korisnicko_ime and korisnik["email"] == email:
            await asyncio.sleep(3)
            print(f"Korisnik pronađen: {korisnik['korisnicko_ime']}")
            await autorizacija(korisnik["korisnicko_ime"], lozinka)
            return True
    await asyncio.sleep(3)
    print(f"Korisnik {korisnicko_ime} nije pronađen.")
    return False


async def autorizacija(korisnik, lozinka):
    for ime in baza_lozinka:
        if ime["korisnicko_ime"] == korisnik:
            if ime["lozinka"] == lozinka:
                await asyncio.sleep(2)
                print(f"Korisnik {korisnik}: Autorizacija uspješna.")
            else:
                print(f"{korisnik}: Autorizacija neuspješna.")


baza_korisnika = [
    {"korisnicko_ime": "mirko123", "email": "mirko123@gmail.com"},
    {"korisnicko_ime": "ana_anic", "email": "aanic@gmail.com"},
    {"korisnicko_ime": "maja_0x", "email": "majaaaaa@gmail.com"},
    {"korisnicko_ime": "zdeslav032", "email": "deso032@gmail.com"},
]

baza_lozinka = [
    {"korisnicko_ime": "mirko123", "lozinka": "lozinka123"},
    {"korisnicko_ime": "ana_anic", "lozinka": "super_teska_lozinka"},
    {"korisnicko_ime": "maja_0x", "lozinka": "s324SDFfdsj234"},
    {"korisnicko_ime": "zdeslav032", "lozinka": "deso123"},
]


async def main():
    rez = await autentifikacija("mirko123", "mirko123@gmail.com", "lozinka123")
    print(rez)


asyncio.run(main())
