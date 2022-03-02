# nti-2022-final

<h3>Задача</h3>
<p>Вам нужно разработать алгоритм, который способен распознать рукописный текст в школьных тетрадях. В качестве входных данных вам будут предоставлены фотографии целых листов. Предсказание модели — список распознанных строк с координатами полигонов и получившимся текстом.</p>
<p>Несмотря на схожесть задачи заключительного этапа с образовательным хакатоном, в котором вы могли принимать участие в феврале, вас ждет пара усложнений:&nbsp;</p>
<ol>
<li>Вас ждет намного больше уникальных стилей в тестовых датасетах, соответственно задача усложняется - придумайте модель, которая способна приспособиться к абсолютно любому почерку в школьных тетрадях!</li>
<li>В выборку добавлен английский язык, так что теперь ваша модель должна быть билингвальной.</li>
</ol>
<p>Мы видим итоговый алгоритм как последовательность двух моделей: сегментации и распознавания. Сначала сегментационная модель предсказывает полигоны маски каждого слова на фото. Затем эти слова вырезаются из изображения по контуру маски (получаются кропы на каждое слово) и подаются в модель распознавания. В итоге получается список распознанных слов с их координатами.</p>
<p>При работе с предоставленными данными поcтарайтесь глубже погрузиться в них и попробовать различные аугментации. Но самое главное: подружите вместе две отдельных модели сегментации и распознавания, для получения качественной и эффективной общей системы.</p>
<p>Материалы, которые могут помочь справиться с задачей:&nbsp;</p>
<ul>
<li><a href="https://youtu.be/mlm2xAg-JpY" rel="noopener noreferrer" target="_blank">Разбор базового решения для модели сегментации</a></li>
<li><a href="https://youtu.be/X7hu8vMM1-s" rel="noopener noreferrer" target="_blank">Разбор базового решения для модели распознавания</a></li>
<li><a href="https://youtu.be/KwVfwnlzLpE" rel="noopener noreferrer" target="_blank">Как собрать докер на примере задачи сегментации</a></li>
<li><a href="https://youtu.be/CQqR5NRvek0" rel="noopener noreferrer" target="_blank">5 идей для решения задач на распознавание текста</a></li>
<li><a href="https://youtu.be/gk20-o2Aktw" rel="noopener noreferrer" target="_blank">Несколько советов от Марка для прошедшего хакатона&nbsp;</a></li>
</ul>
<h3>Формат решений</h3>
<p>В проверяющую систему необходимо отправить код алгоритма, запакованный в ZIP-архив. Решения запускаются в изолированном окружении при помощи Docker. Время и ресурсы во время тестирования ограничены.<br>
В корне архива обязательно должен быть файл <code>metadata.json</code> со структурой:</p>
<pre class="  language-bash"><code class="  language-bash"><span class="token punctuation">{</span>
    <span class="token string">"image"</span><span class="token builtin class-name">:</span> <span class="token string">"&lt;docker image&gt;"</span>,
    <span class="token string">"entry_point"</span><span class="token builtin class-name">:</span> <span class="token string">"&lt;entry point or sh script&gt;"</span>
<span class="token punctuation">}</span></code></pre>
<p>Например:</p>
<pre class="  language-bash"><code class="  language-bash"><span class="token punctuation">{</span>
    <span class="token string">"image"</span><span class="token builtin class-name">:</span> <span class="token string">"skalinin1/baseline-ocr-segm:latest"</span>,
    <span class="token string">"entry_point"</span><span class="token builtin class-name">:</span> <span class="token string">"python run.py"</span>
<span class="token punctuation">}</span></code></pre>
<p>Здесь <code>image</code> – поле с названием docker-образа, в котором будет запускаться решение, <code>entry_point</code> – команда, при помощи которой запускается скрипт инференса. Решение запускается в Docker контейнере. Вы можете воспользоваться готовым образом <code>"skalinin1/baseline-ocr-segm:latest"</code> (создан на основе Dockerfile и <code>requirements.txt</code>, которые находятся в репозитории). При желании вы можете использовать свой образ, выложив его на <a href="https://hub.docker.com" rel="noopener noreferrer" target="_blank">https://hub.docker.com</a>.</p>
<h3>Структура данных</h3>
<p>В контейнер помещается папка <code>images</code>, в которой находятся изображения, на которых необходимо сделать предсказания. Модель должна сформировать файл предсказания формата <code>json</code>, который содержит предсказания для каждого изображения из папки <code>images</code>. Пример содержимого <code>json</code> файла, который должен быть сгенерирован:</p>
<pre class="  language-bash"><code class="  language-bash"><span class="token punctuation">{</span>
<span class="token string">"img_0.jpg"</span><span class="token builtin class-name">:</span> <span class="token punctuation">{</span>
        <span class="token string">"predictions"</span><span class="token builtin class-name">:</span> <span class="token punctuation">[</span>
            <span class="token punctuation">{</span>
                <span class="token string">"polygon"</span><span class="token builtin class-name">:</span> <span class="token punctuation">[</span>
                    <span class="token punctuation">[</span><span class="token number">0</span>, <span class="token number">0</span><span class="token punctuation">]</span>,
                    <span class="token punctuation">[</span><span class="token number">0</span>, <span class="token number">1</span><span class="token punctuation">]</span>,
                    <span class="token punctuation">[</span><span class="token number">1</span>, <span class="token number">0</span><span class="token punctuation">]</span>,
                    <span class="token punctuation">[</span><span class="token number">1</span>, <span class="token number">1</span><span class="token punctuation">]</span>
                <span class="token punctuation">]</span>,
                <span class="token string">"text"</span><span class="token builtin class-name">:</span> <span class="token string">"test"</span>
            <span class="token punctuation">}</span>
        <span class="token punctuation">]</span>
    <span class="token punctuation">}</span>
    <span class="token string">"img_1.jpg"</span><span class="token builtin class-name">:</span> <span class="token punctuation">{</span>
    <span class="token string">"predictions"</span><span class="token builtin class-name">:</span> <span class="token punctuation">[</span>
    <span class="token punctuation">..</span>.
    <span class="token punctuation">]</span>
    <span class="token punctuation">}</span>
<span class="token punctuation">}</span></code></pre>
<p>Пути к данным для изображений (полный путь к папке images) и путь, куда необходимо сохранить результат (файл формата <code>.json</code>) передаются как первые два аргумента при запуске вашего решения. Их можно считать с помощью <code>sys.argv[1:]</code>.</p>
<p><strong>Пример решения</strong><br>
Вам доступен архив <code>sample_submission.zip</code>, в котором содержатся примеры загружаемого решения. В архиве вы найдете следующие файлы:<br>
По данной <a href="https://drive.google.com/file/d/1vaALJAqlmiF-AyOgBjoUgNpNxcm83sd8/view?usp=sharing" rel="noopener noreferrer" target="_blank">ссылке</a> находится архив <code>sample_submission.zip</code>, в котором содержатся примеры загружаемого решения. Следующие файлы в загружаемом архиве необходимы для формирования предсказаний модели:</p>
<ul>
<li><code>metadata.json</code> - обязательный файл для каждого решения; в нём должны быть указаны пути к образу и скрипту выполнения модели</li>
<li><code>run.py</code> - основной скрипт для инференса модели</li>
<li><code>segm-model_final.pth</code> и <code>ocr-model-last.ckpt</code> - веса моделей сегментации и OCR, которые подгружаются во время исполнения скрипта <code>run.py</code></li>
</ul>
<p>Для корректной проверки ваш сабмит должен иметь аналогичную структуру.</p>
<p><strong>Доступные ресурсы:</strong><br>
8 ядер CPU<br>
48Gb RAM<br>
Видеокарта NVidia Tesla V100</p>
<p><strong>Ограничения:</strong><br>
5Gb на архив с решением<br>
25 минут на работу решения</p>
<h3>Метрика</h3>
<p>Метрика качества оценки решений определена в скрипте <code>evaluate.py</code> и представляет собой расчет CER для OCR-модели из пайплайна.</p>
<p>Так как текст распознается на предсказанных моделью полигонах, чтобы понять с каким текстом сравнивать предсказанный моделью, нужно соотнести предсказанные полигоны с ground truth полигонами.</p>
<p>Скрипт <code>evaluate.py</code> для каждого gt-полигона из тетради ищет соответствующий ему предсказанный полигон. Из предсказанных полигонов выбирается тот, который имеет наибольшее пересечение по IoU с gt-полигоном (при этом IoU должно быть больше нуля). Таким образом gt-текст из данного полигона соотносится с предсказанным текстом. Это true positive предсказания.</p>
<p>False negative случаи: если для gt-полигона не был сопоставлен предсказанный полигон, то предсказанный текст для такого полигона устанавливается как пустой "" (т.к. пайплайн не предсказал текст там, где он должен быть).</p>
<p>Для всех false positive предсказанных полигонов (т.е. тех, для которых отсутствуют gt-полигоны) gt-текст устанавливается как пустой "" (т.к. пайплайн предсказал текст там, где его нет).</p>
<p>CER считается по следующей формуле:</p>
<p><mjx-container class="MathJax CtxtMenu_Attached_0" jax="CHTML" display="true" tabindex="0" ctxtmenu_counter="0" style="font-size: 119.6%; position: relative;"><mjx-math display="true" class="MJX-TEX" aria-hidden="true" style="margin-left: 0px; margin-right: 0px;"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D436 TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D438 TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D445 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mfrac space="4"><mjx-frac type="d"><mjx-num><mjx-nstrut type="d"></mjx-nstrut><mjx-mrow><mjx-munderover><mjx-over style="padding-bottom: 0.192em; padding-left: 0.362em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-over><mjx-box><mjx-munder><mjx-row><mjx-base style="padding-left: 0.046em;"><mjx-mo class="mjx-sop"><mjx-c class="mjx-c2211 TEX-S1"></mjx-c></mjx-mo></mjx-base></mjx-row><mjx-row><mjx-under style="padding-top: 0.167em;"><mjx-texatom size="s" texclass="ORD"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-texatom></mjx-under></mjx-row></mjx-munder></mjx-box></mjx-munderover><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D451 TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D461 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D450 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45D TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45F TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D452 TEX-I"></mjx-c></mjx-mi><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D451 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D461 TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45F TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D462 TEX-I"></mjx-c></mjx-mi><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D452 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-mrow></mjx-num><mjx-dbox><mjx-dtable><mjx-line type="d"></mjx-line><mjx-row><mjx-den><mjx-dstrut type="d"></mjx-dstrut><mjx-mrow><mjx-munderover><mjx-over style="padding-bottom: 0.192em; padding-left: 0.362em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-over><mjx-box><mjx-munder><mjx-row><mjx-base style="padding-left: 0.046em;"><mjx-mo class="mjx-sop"><mjx-c class="mjx-c2211 TEX-S1"></mjx-c></mjx-mo></mjx-base></mjx-row><mjx-row><mjx-under style="padding-top: 0.167em;"><mjx-texatom size="s" texclass="ORD"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-texatom></mjx-under></mjx-row></mjx-munder></mjx-box></mjx-munderover><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D459 TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D452 TEX-I"></mjx-c></mjx-mi><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D450 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D461 TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45F TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D462 TEX-I"></mjx-c></mjx-mi><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D452 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-mrow></mjx-den></mjx-row></mjx-dtable></mjx-dbox></mjx-frac></mjx-mfrac></mjx-math><mjx-assistive-mml unselectable="on" display="block"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><mi>C</mi><mi>E</mi><mi>R</mi><mo>=</mo><mfrac><mrow><munderover><mo data-mjx-texclass="OP" movablelimits="false">∑</mo><mrow data-mjx-texclass="ORD"><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mi>d</mi><mi>i</mi><mi>s</mi><msub><mi>t</mi><mi>c</mi></msub><mo stretchy="false">(</mo><mi>p</mi><mi>r</mi><mi>e</mi><msub><mi>d</mi><mi>i</mi></msub><mo>,</mo><mi>t</mi><mi>r</mi><mi>u</mi><msub><mi>e</mi><mi>i</mi></msub><mo stretchy="false">)</mo></mrow><mrow><munderover><mo data-mjx-texclass="OP" movablelimits="false">∑</mo><mrow data-mjx-texclass="ORD"><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mi>l</mi><mi>e</mi><msub><mi>n</mi><mi>c</mi></msub><mo stretchy="false">(</mo><mi>t</mi><mi>r</mi><mi>u</mi><msub><mi>e</mi><mi>i</mi></msub><mo stretchy="false">)</mo></mrow></mfrac></math></mjx-assistive-mml></mjx-container></p>
<p>Здесь <mjx-container class="MathJax CtxtMenu_Attached_0" jax="CHTML" tabindex="0" ctxtmenu_counter="1" style="font-size: 119.6%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D451 TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D461 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D450 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mi>i</mi><mi>s</mi><msub><mi>t</mi><mi>c</mi></msub></math></mjx-assistive-mml></mjx-container> - это расстояние Левенштейна, посчитанное для токенов-символов (включая пробелы), <mjx-container class="MathJax CtxtMenu_Attached_0" jax="CHTML" tabindex="0" ctxtmenu_counter="2" style="font-size: 119.6%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D459 TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D452 TEX-I"></mjx-c></mjx-mi><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D450 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mi>e</mi><msub><mi>n</mi><mi>c</mi></msub></math></mjx-assistive-mml></mjx-container> - длина строки в символах.<br>
Метрика CER изменяется от 0 до 1, где 0 – наилучшее значение, 1 - наихудшее.</p>
<p>IoU – это метрика, которая оценивает степень пересечения между двумя масками (предсказанной и правильной). Она вычисляется как отношение площади пересечения к площади объединения этих двух масок:<br>
<mjx-container class="MathJax CtxtMenu_Attached_0" jax="CHTML" display="true" tabindex="0" ctxtmenu_counter="3" style="font-size: 119.6%; position: relative;"><mjx-math display="true" class="MJX-TEX" aria-hidden="true" style="margin-left: 0px; margin-right: 0px;"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43C TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45C TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D448 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mfrac space="4"><mjx-frac type="d"><mjx-num><mjx-nstrut type="d"></mjx-nstrut><mjx-mrow><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43C TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D461 TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D452 TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45F TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D452 TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D450 TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D461 TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45C TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-mrow></mjx-num><mjx-dbox><mjx-dtable><mjx-line type="d"></mjx-line><mjx-row><mjx-den><mjx-dstrut type="d"></mjx-dstrut><mjx-mrow><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D448 TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45C TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-mrow></mjx-den></mjx-row></mjx-dtable></mjx-dbox></mjx-frac></mjx-mfrac></mjx-math><mjx-assistive-mml unselectable="on" display="block"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><mi>I</mi><mi>o</mi><mi>U</mi><mo>=</mo><mfrac><mrow><mi>I</mi><mi>n</mi><mi>t</mi><mi>e</mi><mi>r</mi><mi>s</mi><mi>e</mi><mi>c</mi><mi>t</mi><mi>i</mi><mi>o</mi><mi>n</mi></mrow><mrow><mi>U</mi><mi>n</mi><mi>i</mi><mi>o</mi><mi>n</mi></mrow></mfrac></math></mjx-assistive-mml></mjx-container></p>
<h3>Baseline</h3>
<p>Вам доступно базовое решение от разработчиков задачи.&nbsp;<br>
В файле <code>baseline.ipynb</code> представлен подход разработчиков задачи к объединению моделей сегментации и распознавания текста. Данный алгоритм не содержит обучение, только объединение 2 уже обученных моделей. Для запуска бейзлайна скачайте данные для обучения, должна получиться следующая структура:</p>
<ul>
<li>baseline.ipynb (основной бейзлайн для текущего хакатона - объединение двух моделей)</li>
<li>segm-model_final.pth (веса модели сегментации)</li>
<li>ocr-model-last.ckpt (веса модели детекции)</li>
<li>baseline_segmentation.ipynb (бейзлайн из 1-ой части олимпиады)</li>
<li>baseline_recognition.ipynb (бейзлайн из 2-ой части олимпиады)</li>
<li>train_segmentation
<ul>
<li>images</li>
<li>annotations.json</li>
<li>annotations_extended.json</li>
<li>binary.npz</li>
</ul>
</li>
<li>train_recognition
<ul>
<li>images</li>
<li>labels.csv</li>
</ul>
</li>
</ul>
<p>Файл <code>baseline_segmentation.ipynb содержит базовое решение для модели сегментации текста. Для запуска модели скачайте данные для обучения и положите их в папку train_segmentation.&nbsp;</code><br>
<code>Файл baseline_recognition.ipynb содержит базовое решение для модели распознавания текста. Для запуска модели скачайте данные для обучения и положите их в папку train_recognition.&nbsp;</code></p>
