def main():
    party_list=['Stas','Igor','Zarina','Mother','Father']
    for name_for_invite in party_list:
        print(f"Dear {name_for_invite.title()}, glad to see you in my birthday at 12 january")
    print(f"\n{party_list[0]} will not to go at my birthday!\n")
    party_list[0]='Katya'
    for new_names_to_party in party_list:
        print(f'{new_names_to_party.title()} will go to my party!')
    print("\nNow I've got a new table! And i can invite three more people!\n")
    party_list.insert(0,'Semen')
    party_list.insert(3,"Rustam")
    party_list.append("Diana")
    for new_table_names in party_list:
        print(f'{new_table_names.title()} will go to my party!')
    print("\nI'm sorry, but new table will not arrive at time, and i must decide only two people, who go at my birthday :(\n")
    count_table_people=len(party_list)-2
    for pop_guest in range(count_table_people):
        print(f"{party_list.pop(-1)} will not go at my party")
    print()
    for finish_list_of_guests in party_list:
        print(f"{finish_list_of_guests} will go at my party!")
    del party_list[0]
    del party_list[0]
    print(party_list)
main()