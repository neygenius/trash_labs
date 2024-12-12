namespace Lab1_NenashevDM_6413;

public class ArithmeticalAlgorithm
{
    private class SymbolProbability
    {
        public char Symbol { get; set; }
        public decimal Probability { get; set; }

        public SymbolProbability(char symbol, decimal probability)
        {
            Symbol = symbol;
            Probability = probability;
        }
    }

    private List<SymbolProbability> probabilities;

    public string Encode(string input)
    {
        probabilities = CalculateProbabilities(input);
        decimal low = 0;
        decimal high = 1;

        foreach (char symbol in input)
        {
            decimal range = high - low;
            var probSymbol = probabilities.First(p => p.Symbol == symbol);
            high = low + range * (probSymbol.Probability + GetCumulativeProbability(probSymbol));
            low = low + range * GetCumulativeProbability(probSymbol);
        }

        return EncodeToString(low, high);
    }

    public string Decode(string encoded, int length)
    {
        decimal value = decimal.Parse(encoded);
        decimal low = 0;
        decimal high = 1;
        string decodedString = string.Empty;

        for (int i = 0; i < length; i++)
        {
            decimal range = high - low;
            decimal scaledValue = (value - low) / range;

            SymbolProbability symbol = probabilities.First(prob =>
                GetCumulativeProbability(prob) <= scaledValue &&
                scaledValue < GetCumulativeProbability(prob) + prob.Probability);

            if (symbol == null)
            {
                throw new InvalidOperationException("Symbol not found during decoding.");
            }

            decodedString += symbol.Symbol;

            high = low + range * (GetCumulativeProbability(symbol) + symbol.Probability);
            low = low + range * (GetCumulativeProbability(symbol));
        }

        return decodedString;
    }

    private List<SymbolProbability> CalculateProbabilities(string input)
    {
        var frequencies = input.GroupBy(c => c)
                               .ToDictionary(g => g.Key, g => (decimal)g.Count() / input.Length);
        return frequencies.Select(kvp => new SymbolProbability(kvp.Key, kvp.Value))
                          .OrderBy(p => p.Symbol)
                          .ToList();
    }

    private decimal GetCumulativeProbability(SymbolProbability symbol)
    {
        return probabilities.TakeWhile(p => p.Symbol < symbol.Symbol).Sum(p => p.Probability);
    }

    private string EncodeToString(decimal low, decimal high)
    {
        decimal average = (low + high) / 2;
        return average.ToString();
    }
}