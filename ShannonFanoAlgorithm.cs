namespace Lab1_NenashevDM_6413;

public class ShannonFanoAlgorithm
{
    private Dictionary<char, string> codes = new Dictionary<char, string>();
    private Dictionary<string, char> reverseCodes = new Dictionary<string, char>();

    public string Encode(string input)
    {
        // Считаем частоты символов
        var frequency = GetFrequency(input);
        // Создаем таблицу кодов
        CreateCodes(frequency);
        // Кодируем строку
        return string.Join("", input.Select(c => codes[c]));
    }

    public string Decode(string encoded)
    {
        string decodedString = "";
        string temp = "";

        // Декодируем строку по коду
        foreach (char bit in encoded)
        {
            temp += bit;
            if (reverseCodes.TryGetValue(temp, out char symbol))
            {
                decodedString += symbol;
                temp = ""; // сбрасываем временной код
            }
        }

        return decodedString;
    }

    private Dictionary<char, int> GetFrequency(string input)
    {
        return input.GroupBy(c => c)
                    .ToDictionary(g => g.Key, g => g.Count());
    }

    private void CreateCodes(Dictionary<char, int> frequency)
    {
        var sortedSymbols = frequency.OrderByDescending(x => x.Value).Select(x => x.Key).ToList();
        codes.Clear();
        reverseCodes.Clear();
        GenerateCodes(sortedSymbols, "", frequency);
    }

    private void GenerateCodes(List<char> symbols, string prefix, Dictionary<char, int> frequency)
    {
        if (symbols.Count == 1)
        {
            codes[symbols[0]] = prefix;
            reverseCodes[prefix] = symbols[0];
            return;
        }

        // Разделяем символы на две группы
        int total = symbols.Sum(c => frequency[c]);
        int cumFreq = 0;
        int splitIndex = 0;

        for (int i = 0; i < symbols.Count; i++)
        {
            cumFreq += frequency[symbols[i]];
            if (cumFreq >= total / 2)
            {
                splitIndex = i + 1;
                break;
            }
        }

        var leftSymbols = symbols.Take(splitIndex).ToList();
        var rightSymbols = symbols.Skip(splitIndex).ToList();

        // Рекурсивно создаем коды для обеих групп
        GenerateCodes(leftSymbols, prefix + "0", frequency);
        GenerateCodes(rightSymbols, prefix + "1", frequency);
    }
}
