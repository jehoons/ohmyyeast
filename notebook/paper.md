# todo 

--- 현재 상황은 

수학모델을 설명하는 부분에 대해서 전반적으로 설명을 개선해야하지 않나 하는 생각이 들었습니다. 예를 들면, 시너지스코어나 코어스트럭쳐와 같은 용어들이 이해되기 쉽도록 대체할 수 있는 용어가 있다면 교체해야 하고, 분석내용을 보다 쉽게 이해할수 있도록 하는 설명방식을 고민할 필요가 있습니다.  

리뷰어가 지적한 문제들 중에서 (모델링 부분에서) 가장 중요한 부분은 Fig 2의 region-1, region-2를 구분하는 경계에 대한 다음과 같은 3개의 문제라고 생각이 되었습니다.  

a. 경계를 어떻게 설정하였는가? 

b. 경계의 변화에 대해서 결과가 일정하게 나오는가?

c. 경계의 위치를 최적화할 수 있는가?  

경계의 설정이 합리적인 방식으로 이루어 지지 않았다면, 그리고 결과에 대해서 robust하지 않다면 이로부터 도출되는 모든 다른 결과들이 유효하지 않을 것이라고 리뷰어가 지적하였습니다. 제 생각에도 언제든 지적받을 수 있는 문제로 생각이 됩니다. 질문 b에 대해서는 답변을 하기 위해 계산코드를 작성하고 있는 중에 있습니다. c의 경우에는 아이디어를 좀 개발해야할 필요가 있습니다. c에 대해서 답변을 하는 것이 가능하다면 a에 대해서도 답변이 될 것입니다. 

진행방향..

오늘 중으로 이메일 회람하기

핵심 리뷰어 코멘트 - 리마인드. 

2.3일

--- 


Reviewer #4
-----------

> The manuscript does not even mention any details about the modeling approach (ode model or Boolean?, Michaelis Menten or linear kinetics? Which optimization routine?) and does not provide the definition to terms like “core structure” or “synergy score”, so that the reader has to consult the (incomplete) supplementary methods to fully understand the manuscript.

이 연구에서 사용한 접근방법은 ode접근방법이었고 신호전달경로의 근사를 위해서 MM을 가정하였다. 최적화는 유전자알고리즘을 사용하였다. 

코어스트럭처의 정의: Core structure is defined by invariable k edges. 여기서 2개의 엣지는 11->7, 7->3 이며 언제나 필수적인 것으로 간주한다. 그러므로 우리는 k-2개의 엣지만을 이용하여 코어구조를 정의할 수 있다. 3개의 노드를 연결하는 최대 9개의 엣지가 존재할 수 있다. 여기서 코어구조로 선택하고 남은 엣지들은 variable edge들이다. 이들은 자유롭게 변할 수 있다. variable edge들로 인해서 k-edges로 구성되는 코어스트럭처는 3^(9-k)개 만큼의 variations를 가질 수 있다. 그러므로 k개의 edge와 9-k개 만큼의 variations를 가질수 있게 된다. 

core structure analysis identifies a set of invariable edges that defines core structure (Extended Figure 5A). The core structure is identified as follows: 

e has the smallest prediction error by measuring fitness score of intact structure, core structure analysis identifies a set of invariable edges that defines core structure (Extended Figure 5A). The core structure is identified as follows: 

시너지 스코어의 정의 - 


> The authors then try to fit a rather generic model of the MAPK signaling pathway where they added additional edges to the model, and ranked these models based on the goodness of fit. The details of this analysis are unclear, as they are not described in the methods. 

mathematical model, core structure analysis에서 기술했지만... 조금 더.. 

> Apparently, the authors used a genetic algorithm to fit parameters, and left the algorithm running multiple times which found multiple (local) optima, as the fitness error shows large errors for many models (Fig. 2b). 

> This is a clear indication that most model parameters cannot be determined from the data (the models are underdetermined) and the optimizer gets stuck in local minima. This is not a good strategy, as if the optimizer often gets stuck in those local optima, it is unclear if better fits exists. 

여기서, 파라미터는 상대적으로 덜 중요하다. 중요한 것은 동일구조를 최적화할때 나오는 평균적인 성능이 어떤것이 도 좋은가를 평가하는 것이기 때문이다.  
> Moreover, it is completely unclear which parameter set would describe the pathway best (which is however needed to make the sensitivitiy analysis).   A core structure is defined as a set of invariable edges. All structures that contain these invariable edges are member structures, independent of all other possible edges being negative, positive or absent. Core structures are evaluated according to the ratio of their relative abundances in region 1 and region 2, named Ar here. The synergistic score weighs Ar of a specific core structure in relation to the sum of all Ar values of the single edges that define a core structure. 

최종적인 결론은 보더에 상당히 민감할 수가 있다. 그런데, 그 보더를 어떻게 설정했는지도 분명하지가 않다. 
> However, this means that the entire analysis critically depends on the seperation of region 1 and region 2 – and this seperation coinsides with the increased difficulty to obtain optima in region. But this is classification based on technical / numerical problems. The authors refer to fig. 2B which does not explain how the border was set. 

현재, 보더는 fitness의 기울기를 이용하여 설정하였다. 보더를 다른 변수들에 종속적으로 설정할수 있는가? 

> The other reference goes to Extended Data Table 3, which lists the best core structures with 1 to 7 invariable edges, which does not help to indentify the border between these two regions.

> Minor comments:  Presentation of the 2d data in Fig. 1c is suboptimal, the “fit” (how is it fitted, why?) suggests certain behavior, but the data is notvisible. Visualization of the raw data as heatmap might be one option, or having multiple 1d-plots (like the insets) could be another option.   - Whats the meaning of the errorbars on the Fitness error? Does it stem from running the fitting routine several times? The genetic algorithm produces slightly different model fits each time you run it, however, if the fluctuation of the fitness error is as high as indicated here, most models will not significantly differ in their ability to explain the data! - in general, the approach to rank model structure is ad-hoc. A rigorous analysis would have to deal with the fact that different models have different numbers of parameters, it would consider experimental error from replicate measurements. Then one could use a likelihood-based approach (AIC, BIC, ratio test etc).  - how many datapoints do we have exactly to parameterise the model (not clear from figure 1) - are parameters identifiable then? - how did you estimate the parameters of the algebraic equation that connects Fus3 activity with Fus1 reporter output? - is the mode parameter fitted in steady state? This seems reasonable, but then the model is overparameterised. 



