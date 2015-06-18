__author__ = 'sheldon'
def boiler():
    from boilerpipe.extract import Extractor
    for i in range(0, 1000):
        input_filename = 'page/' + str(i) + '.txt'
        output_filename = 'boilerpipe/' + str(i) + '.txt'
        input_file = open(input_filename, 'r')
        s = input_file.read()
        input_file.close()
        extractor = Extractor(extractor='ArticleExtractor', html=s.decode('GBK', 'ignore'))
        output_file = open(output_filename, 'wb')
        output_file.write(extractor.getText().encode('utf-8'))
        output_file.close()
def goose_test():
    from goose import Goose
    from goose.text import StopWordsChinese
    for i in range(0, 1000):
        input_filename = 'page/' + str(i) + '.txt'
        output_filename = 'goose/' + str(i) + '.txt'
        input_file = open(input_filename, 'r')
        s = input_file.read()
        input_file.close()
        g = Goose({'stopwords_class': StopWordsChinese})
        article = g.extract(raw_html=s)
        output_file = open(output_filename, 'wb')
        output_file.write(article.cleaned_text.encode('utf-8'))
        output_file.close()
def dragnet_test():
    from dragnet import content_extractor
    for i in range(0, 1000):
        input_filename = 'page/' + str(i) + '.txt'
        output_filename = 'dragnet/' + str(i) + '.txt'
        input_file = open(input_filename, 'r')
        s = input_file.read()
        input_file.close()
        article = content_extractor.analyze(s)
        output_file = open(output_filename, 'wb')
        output_file.write(article)
        output_file.close()
def newspaper_test():
    from newspaper import fulltext, Article
    for i in range(0, 1000):
        input_filename = 'page/' + str(i) + '.txt'
        output_filename = 'newspaper/' + str(i) + '.txt'
        input_file = open(input_filename, 'r')
        s = input_file.read()
        input_file.close()
        a = Article(language='zh')
        a.html = s
        a.parse()
        # print a.text
        raw_input('wait')
        # article = fulltext(s, language='zh')
        # output_file = open(output_filename, 'wb')
        # output_file.write(article)
        # output_file.close()
if __name__ == '__main__':
    from timeit import Timer
    result = open('time.txt', 'wb')

    boilerTime = Timer('boiler()', 'from __main__ import boiler')
    time = boilerTime.timeit(1)
    print time
    result.write(str(time))
    result.write('\n')

    gooseTime = Timer('goose_test()', 'from __main__ import goose_test')
    time = gooseTime.timeit(1)
    print time
    result.write(str(time))
    result.write('\n')

    dragnetTime = Timer('dragnet_test()', 'from __main__ import dragnet_test')
    time = dragnetTime.timeit(1)
    print time
    result.write(str(time))

    # newspaperTime = Timer('newspaper_test()', 'from __main__ import newspaper_test')
    # time = newspaperTime.timeit(1)
    # print time
    # result.write(str(time))
    result.close()
