"""Platform for sensor integration."""
from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import TEMP_CELSIUS
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from datetime import timedelta, datetime, date

MIN_TIME_BETWEEN_SCANS = timedelta(seconds=3600)

seznam = [[""],
        ["", "Nový rok", "Karina", "Radmila", "Diana", "Dalimil", "!tři králové", "Vilma", "Čestmír", "Vladan", "Břetislav", "Bohdana", "Pravoslav", "Edita", "Radovan", "Alice", "Ctirad", "Drahoslav", "Vladislav", "Doubravka", "Ilona", "Běla", "Slavomír", "Zdeněk", "Milena", "Miloš", "Zora", "Ingrid", "Otýlie", "Zdislava", "Robin", "Marika"],
        ["", "Hynek", "Nela", "Blažej", "Jarmila", "Dobromila", "Vanda", "Veronika", "Milada", "Apolena", "Mojmír", "Božena", "Slavěna", "Věnceslav", "Valentýn", "Jiřina", "Ljuba", "Miloslava", "Gizela", "Patrik", "Oldřich", "Lenka", "Petr", "Svatopluk", "Matěj", "Liliana", "Dorota", "Alexandr", "Lumír", "Horymír"],
        ["", "Bedřich", "Anežka", "Kamil", "Stela", "Kazimír", "Miroslav", "Tomáš", "Gabriela", "Františka", "Viktorie", "Anděla", "Řehoř" ,"Růžena" ,"Root / Matylda" ,"Ida" ,"Elena / Herbert" ,"Vlastimil" ,"Eduard" ,"Josef" ,"Světlana" ,"Radek" ,"Leona" ,"Ivona" ,"Gabriel" ,"Marián" ,"Emanuel" ,"Dita" ,"Soňa" ,"Taťána" ,"Arnošt" ,"Kvido"],
        ["", "Hugo" ,"Erika" ,"Richard" ,"Ivana" ,"Miroslava" ,"Vendula" ,"Heřman / Hermína" ,"Ema" ,"Dušan" ,"Darja" ,"Izabela" ,"Julius" ,"Aleš" ,"Vincenc" ,"Anastázie" ,"Irena" ,"Rudolf" ,"Valérie" ,"Rostislav" ,"Marcela" ,"Alexandra" ,"Evženie" ,"Vojtěch" ,"Jiří" ,"Marek" ,"Oto" ,"Jaroslav" ,"Vlastislav" ,"Robert" ,"Blahoslav"],
        ["", "!svátek práce" ,"Zikmund" ,"Alexej" ,"Květoslav" ,"Klaudie" ,"Radoslav" ,"Stanislav" ,"!den osvobození" ,"Ctibor" ,"Blažena" ,"Svatava" ,"Pankrác" ,"Servác" ,"Bonifác" ,"Žofie" ,"Přemysl" ,"Aneta" ,"Nataša" ,"Ivo" ,"Zbyšek" ,"Monika" ,"Emil" ,"Vladimír" ,"Jana" ,"Viola" ,"Filip" ,"Valdemar" ,"Vilém" ,"Maxmilián" ,"Ferdinand" ,"Kamila"],
        ["", "Laura" ,"Jarmil" ,"Tamara" ,"Dalibor" ,"Dobroslav" ,"Norbert" ,"Iveta / Slavoj" ,"Medard" ,"Stanislava" ,"Gita" ,"Bruno" ,"Antonie" ,"Antonín" ,"Roland" ,"Vít" ,"Zbyněk" ,"Adolf" ,"Milan" ,"Leoš" ,"Květa" ,"Alois" ,"Pavla" ,"Zdeňka" ,"Jan" ,"Ivan" ,"Adriana" ,"Ladislav" ,"Lubomír" ,"Petr / Pavel" ,"Šárka"],
        ["", "Jaroslava" ,"Patricie" ,"Radomír" ,"Prokop" ,"Ciril & Metoděj" ,"+ Jan Hus" ,"Bohuslava" ,"Nora" ,"Drahoslava" ,"Libuše / Amálie" ,"Olga" ,"Bořek" ,"Markéta" ,"Karolína" ,"Jindřich" ,"Luboš" ,"Martina" ,"Drahomíra" ,"Čeněk" ,"Ilja" ,"Vítězslav" ,"Magdaléna" ,"Libor" ,"Kristýna" ,"Jakub" ,"Anna" ,"Věroslav" ,"Viktor" ,"Marta" ,"Bořivoj" ,"Ignác"],
        ["", "Oskar" ,"Gustav" ,"Miluše" ,"Dominik" ,"Kristián" ,"Oldřiška" ,"Lada" ,"Soběslav" ,"Roman" ,"Vavřinec" ,"Zuzana" ,"Klára" ,"Alena" ,"Alan" ,"Hana" ,"Jáchym" ,"Petra" ,"Helena" ,"Ludvík" ,"Bernard" ,"Johana" ,"Bohuslav" ,"Sandra" ,"Bartoloměj" ,"Radim" ,"Luděk" ,"Otakar" ,"Augustýn" ,"Evelína" ,"Vladěna" ,"Pavlína"],
        ["", "Linda / Samuel" ,"Adéla" ,"Bronislav" ,"Jindřiška" ,"Boris" ,"Boleslav" ,"Regína" ,"Mariana" ,"Daniela" ,"Irma" ,"Denisa" ,"Marie" ,"Lubor" ,"Radka" ,"Jolana" ,"Ludmila" ,"Naděžda" ,"Kryštof" ,"Zita" ,"Oleg" ,"Matouš" ,"Darina" ,"Berta" ,"Jaromír" ,"Zlata" ,"Andrea" ,"Jonáš" ,"Václav" ,"Michal" ,"Jeroným"],
        ["", "Igor" ,"Olívie / Oliver" ,"Bohumil" ,"František" ,"Eliška" ,"Hanuš" ,"Justýna" ,"Věra" ,"Štefan / Sára" ,"Marina" ,"Andrej" ,"Marcel" ,"Renáta" ,"Agáta" ,"Tereza" ,"Havel" ,"Hedvika" ,"Lukáš" ,"Michaela" ,"Vendelín" ,"Brigita" ,"Sabina" ,"Teodor" ,"Nina" ,"Beáta" ,"Erik" ,"Šarlota / Zoe" ,"státní svátek" ,"Silvie" ,"Tadeáš" ,"Štěpánka"],
        ["", "Felix" ,"!památka zesnulých" ,"Hubert" ,"Karel" ,"Miriam" ,"Liběna" ,"Saskie" ,"Bohumír" ,"Bohdan" ,"Evžen" ,"Martin" ,"Benedikt" ,"Tibor" ,"Sáva" ,"Leopold" ,"Otmar" ,"Mahulena" ,"Romana" ,"Alžběta" ,"Nikola" ,"Albert" ,"Cecílie" ,"Klement" ,"Emílie" ,"Kateřina" ,"Artur" ,"Xenie" ,"René" ,"Zina" ,"Ondřej"],
        ["", "Iva" ,"Blanka" ,"Svatoslav" ,"Barbora" ,"Jitka" ,"Mikuláš" ,"Benjamín" ,"Květoslava" ,"Vratislav" ,"Julie" ,"Dana" ,"Simona" ,"Lucie" ,"Lýdie" ,"Radana / Radan" ,"Albína" ,"Daniel" ,"Miloslav" ,"Ester" ,"Dagmar" ,"Natálie" ,"Šimon" ,"Vlasta" ,"Adam / Eva" ,"1.svátek vánoční" ,"Štěpán" ,"Žaneta" ,"Bohumila" ,"Judita" ,"David" ,"Silvestr"]] 

def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None
) -> None:
    """Set up the sensor platform."""
    add_entities([CZSvatekSensor()])


class CZSvatekSensor(SensorEntity):
    """Representation of a Sensor."""

    _attr_name = "Svátek dnes"
    
    #@Throttle(MIN_TIME_BETWEEN_SCANS)
    def update(self) -> None:
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        ted = datetime.now()
        jmeno = seznam[int(ted.strftime("%m"))][int(ted.strftime("%d"))]
        self._attr_native_value = jmeno
