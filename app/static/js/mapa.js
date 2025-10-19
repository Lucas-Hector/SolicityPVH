
const dadosBairros = {
    "1": { nome: "Floresta", solicitacoes: 0 },
    "2": { nome: "Nacional", solicitacoes: 50 },
    "3": { nome: "Mato Grosso", solicitacoes: 0 },
    "4": { nome: "Castanheira", solicitacoes: 0 },
    "5": { nome: "Pantanal", solicitacoes: 0 },
    "6": { nome: "Caladinho", solicitacoes: 0 },
    "7": { nome: "Ulysses Guimarães", solicitacoes: 0 },
    "8": { nome: "Industrial", solicitacoes: 0 },
    "9": { nome: "Cohab", solicitacoes: 9 },
    "10": { nome: "São Francisco", solicitacoes: 7 },
    "11": { nome: "Marcos Freire", solicitacoes: 12 },
    "12": { nome: "Ronaldo Aragão", solicitacoes: 7 },
    "13": { nome: "Igarapé", solicitacoes: 15 },
    "14": { nome: "Nova Floresta", solicitacoes: 9 },
    "15": { nome: "Caiari", solicitacoes: 30 },
    "16": { nome: "Mariana", solicitacoes: 31 },
    "17": { nome: "Cidade Jardim", solicitacoes: 32 },
    "18": { nome: "Novo Horizonte", solicitacoes: 33 },
    "19": { nome: "Agenor de Carvalho", solicitacoes: 34 },
    "20": { nome: "Triângulo", solicitacoes: 35 },
    "21": { nome: "Nova Porto Velho", solicitacoes: 36 },
    "22": { nome: "Cascalheira", solicitacoes: 48 },
    "23": { nome: "Centro", solicitacoes: 45 },
    "24": { nome: "São João Bosco", solicitacoes: 41 },
    "25": { nome: "Arigolândia", solicitacoes: 0 },
    "26": { nome: "Bairro Novo", solicitacoes: 49 },
    "27": { nome: "Jardim Santana", solicitacoes: 55 },
    "28": { nome: "Maringá", solicitacoes: 75 },
    "29": { nome: "Socialista", solicitacoes: 85 },
    "30": { nome: "Pedrinhas", solicitacoes: 0 },
    "31": { nome: "Nossa Senhora das Graças", solicitacoes: 120 },
    "32": { nome: "Area Militar e Aeroporto", solicitacoes: 7 },
    "33": { nome: "Tomé de Souza", solicitacoes: 15 },
    "34": { nome: "Esperança da Comunidade", solicitacoes: 62 },
    "35": { nome: "Areal", solicitacoes: 7 },
    "36": { nome: "Baixa União", solicitacoes: 9 },
    "37": { nome: "Militar", solicitacoes: 15 },
    "38": { nome: "Eldorado", solicitacoes: 90 },
    "39": { nome: "Lagoa", solicitacoes: 9 },
    "40": { nome: "Cidade Nova", solicitacoes: 7 },
    "41": { nome: "Escola de Polícia", solicitacoes: 12 },
    "42": { nome: "Panair", solicitacoes: 7 },
    "43": { nome: "Aeroclube", solicitacoes: 15 },
    "44": { nome: "Três Marias", solicitacoes: 9 },
    "45": { nome: "Cidade do Lobo", solicitacoes: 7 },
    "46": { nome: "Conceição", solicitacoes: 12 },
    "47": { nome: "São Sebastião", solicitacoes: 15 },
    "48": { nome: "Eletronorte", solicitacoes: 86 },
    "49": { nome: "Areia Branca", solicitacoes: 47 },
    "50": { nome: "Santa Bárbara", solicitacoes: 7 },
    "51": { nome: "Mocambo", solicitacoes: 0 },
    "52": { nome: "Tancredo Neves", solicitacoes: 7 },
    "53": { nome: "Lagoinha", solicitacoes: 36 },
    "54": { nome: "Juscelino Kubitscheck", solicitacoes: 9 },
    "55": { nome: "Cuniã", solicitacoes: 7 },
    "56": { nome: "Tiradentes", solicitacoes: 9 },
    "57": { nome: "Liberdade", solicitacoes: 0 },
    "58": { nome: "Km-1", solicitacoes: 15 },
    "59": { nome: "Olaria", solicitacoes: 9 },
    "60": { nome: "São Cristóvão", solicitacoes: 7 },
    "61": { nome: "Flodoaldo Pontes Pinto", solicitacoes: 63 },
    "62": { nome: "Embratel", solicitacoes: 7 },
    "63": { nome: "Rio Madeira", solicitacoes: 15 },
    "64": { nome: "Aponiã", solicitacoes: 9 },
    "65": { nome: "Teixeirão", solicitacoes: 7 },
    "66": { nome: "Planalto", solicitacoes: 9 },
    "67": { nome: "Tucumanzal", solicitacoes: 15 },
    "68": { nome: "Nova Esperança", solicitacoes: 101 },
    "69": { nome: "Costa e Silva", solicitacoes: 0 },
    "70": { nome: "Roque", solicitacoes: 0 },
    "71": { nome: "Tupy", solicitacoes: 0 },
    "72": { nome: "Roque", solicitacoes: 0 }
};

function calcularCor(solicitacoes) {
    cor = "#fff"
    
    if (solicitacoes == 0){
        cor = "#a1d9ff"
    } else if (solicitacoes >=1 && solicitacoes <= 20){
        cor = "#61b5e6"
    } else if (solicitacoes >=21 && solicitacoes <= 40){
        cor = "#2e88d1"
    } else if (solicitacoes >=41 && solicitacoes <= 60){
        cor = "#0b6cad"
    } else if (solicitacoes >=61 && solicitacoes <= 80){
        cor = "#096885"
    } else if (solicitacoes >=81 && solicitacoes <= 100){
        cor = "#033a4b"
    } else if (solicitacoes > 100) {
        cor = "#001069"
    }

    return cor;
}

// --- Carrega o SVG ---
fetch("../static/img/ba_bairros_colorido.svg")
    .then(res => res.text())
    .then(svgData => {
        document.getElementById("mapa").innerHTML = svgData;

        const tooltip = document.getElementById("tooltip");
        const svg = document.querySelector("#mapa svg");

        const regioes = svg.querySelectorAll("path, polygon, rect");

        regioes.forEach((regiao, index) => {
            const id = regiao.id || index + 1;
            const info = dadosBairros[id];
            
            if (info) {
                // Define a cor 
                regiao.setAttribute("fill", calcularCor(info.solicitacoes));
            } else {
                regiao.setAttribute("fill", "#76d5f1"); 
            }

            regiao.addEventListener("mousemove", e => {
                if (info) {
                    const tooltipWidth = tooltip.offsetWidth;
                    const tooltipHeight = tooltip.offsetHeight;
                
                    const posX = e.pageX - tooltipWidth + 100; 
                    const posY = e.pageY - tooltipHeight 
                
                    tooltip.textContent = `${info.nome}
                        Solicitações: ${info.solicitacoes}
                    `;
                                
                    tooltip.style.left = posX + "px";
                    tooltip.style.top = posY + "px";
                    tooltip.style.opacity = 1;
                    regiao.classList.add("highlight");
                }
            });
            
            regiao.addEventListener("mouseleave", () => {
                tooltip.style.opacity = 0;
                regiao.classList.remove("highlight");
            });
        });
    }
);
