import os
def main():
    population_list=[]
    delta_list=[]
    years_list=[year for year in range(1950,1991)]
    population_file=open("USPopulation.txt","r")
    years_population=population_file.readline()
    while years_population!='':
        years_population=years_population.rstrip("\n")
        population_list.append(int(years_population))
        years_population = population_file.readline()
    population_file.close()

    for index in range(len(population_list)-1):
        yearly_change=population_list[index+1]-population_list[index]
        delta_list.append(yearly_change)
    average_annual=sum(delta_list)/len(delta_list)
    max_delta=max(delta_list)
    max_year=years_list[delta_list.index(max_delta)+1]
    min_delta=min(delta_list)
    min_year=years_list[delta_list.index(min_delta)+1]
    print(f'Среднегодовое увеличение населения равно {average_annual:.0f}, год с максимальным увеличением-{max_year}, год с минимальным приростом-{min_year}.')
    #print(f"{len(delta_list)}")
    #print(delta_list)
main()

