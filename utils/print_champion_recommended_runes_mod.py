from bs4 import BeautifulSoup
from .extract_div_html_mod import extract_div_html



def print_champion_recommended_runes(champion_name):

    try:
        soup = BeautifulSoup(extract_div_html(f'https://u.gg/lol/champions/{champion_name.lower()}/build?rank=overall', 'rune-trees-container-2 media-query media-query_MOBILE_LARGE__DESKTOP_LARGE'), 'lxml')

        primary_tree = soup.find(class_='primary-tree')
        primary_tree_name = primary_tree.find(class_='perk-style-title').text
        resolve_keystone = primary_tree.find(class_='perk keystone perk-active')
        resolve_runes = primary_tree.find_all(class_='perk perk-active')

        secondary_tree = soup.find(class_='secondary-tree')
        secondary_tree_name = secondary_tree.find(class_='perk-style-title').text
        inspiration_keystone = secondary_tree.find(class_='perk perk-active')
        inspiration_runes = secondary_tree.find_all(class_='perk perk-active')

        stat_shards = soup.find(class_='stat-shards-container_v2')
        stat_shard_rows = stat_shards.find_all(class_='perk-row stat-shard-row')
        stat_shards_active = [row.find(class_='shard shard-active') for row in stat_shard_rows]

        primary_runes = [resolve_keystone.img['alt']] + [rune.img['alt'] for rune in resolve_runes]
        secondary_runes = [inspiration_keystone.img['alt']] + [rune.img['alt'] for rune in inspiration_runes]
        stat_shards = [shard.img['alt'] for shard in stat_shards_active]

        return primary_tree_name, primary_runes, secondary_tree_name, secondary_runes, stat_shards
    
    except:
        print("Champion not found.")
        return None, None, None, None, None

    # print(f"Recommended Runes for {champion_name.capitalize()}: \n")

    # print(f"Primary Tree : {primary_tree_name}\n ")
    # print("Primary Runes:")
    # for rune in list(dict.fromkeys(primary_runes)):
    #     print(rune.replace('The Rune', '').replace("The Keystone",'').strip())

    # print(f"\nSecondary Tree : {secondary_tree_name}\n")
    # print("Secondary Runes:")
    # for rune in list(dict.fromkeys(secondary_runes)):
    #     print(rune.replace('The Rune', '').strip())

    # print("\nStat Shards:")
    # for shard in list(dict.fromkeys(stat_shards)):
    #     print(shard.replace('The','').replace('Shard', '').strip())
