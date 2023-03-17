import { classNames } from 'shared/lib/classNames/classNames';
import { Page } from 'widgets/Page/Page';
import React, { memo, useCallback, useState } from 'react';
import { RadarDiagram } from 'shared/UI/RadarDiagram';
import { Card } from 'shared/UI/Card';
import { Modal } from 'react-bootstrap';
import {
    Bar, BarChart, CartesianGrid, Legend, Tooltip, XAxis, YAxis,
} from 'recharts';
import classes from './MainPage.module.scss';

interface MainPageProps {
    className?: string;
}

const data = [
    {
        subject: 'Frontend Developing',
        A: 9,
        fullMark: 10,
    },
    {
        subject: 'Backend Developing',
        A: 6,
        fullMark: 10,
    },
    {
        subject: 'Android Developing',
        A: 2,
        fullMark: 10,
    },
    {
        subject: 'QA Engineer',
        A: 2,
        fullMark: 10,
    },
    {
        subject: 'Java Developer',
        A: 2,
        fullMark: 10,
    },
    {
        subject: 'Go Developer',
        A: 3,
        fullMark: 10,
    },
];
const specData = [
    {
        name: 'HTML',
        score: 10,
    },
    {
        name: 'CSS',
        score: 9,
    },
    {
        name: 'Javascript',
        score: 8,
    },
    {
        name: 'Usage of Git',
        score: 8,
    },
    {
        name: 'Package Managers',
        score: 6,
    },
    {
        name: 'Build Tools',
        score: 6,
    },
    {
        name: 'CSS Frameworks',
        score: 7,
    },
];

const specialization = 'Создание защищенного ПО';

const MainPage = memo((props: MainPageProps) => {
    const {
        className,
    } = props;

    const [show, setShow] = useState<boolean>(false);
    const [specializationInfo, setSpecializationInfo] = useState<string>('');

    const onLabelClickHandler = useCallback((e) => {
        if (e) {
            setShow(true);
            setSpecializationInfo(e.activeLabel);
            console.log(e.activeLabel);
        }
    }, []);

    return (
        <Page className={classNames(classes.MainPage, {}, [className])}>
            <Modal
                centered
                fullscreen
                show={show}
                onHide={() => setShow(false)}
            >
                <Modal.Header closeButton>
                    <Modal.Title>{specializationInfo}</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <BarChart
                        width={1000}
                        height={300}
                        data={specData}
                    >
                        <CartesianGrid strokeDasharray="2 2" />
                        <XAxis dataKey="name" />
                        <YAxis domain={[0, 10]} />
                        <Bar
                            barSize={75}
                            className={classes.bar}
                            dataKey="score"
                            stackId="a"
                        />
                    </BarChart>
                </Modal.Body>
            </Modal>

            <Card className={classes.mainInfo}>
                <h2>
                    Корчак Родион Дмитриевич
                </h2>
                <p>
                    {`Специализация: ${specialization}`}
                </p>
            </Card>
            <Card className={classes.year}>
                <h3>Военно-космическая Орденов Жукова и Красного знамени академия имени А.Ф. Можайского</h3>
                <h3>Год выпуска: 2026</h3>
            </Card>
            <Card className={classes.addIndo}>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias culpa eligendi et, harum nam nemo nihil quas qui quidem sit.</Card>
            <Card className={classes.skills}>
                <h2>Умения</h2>
                <RadarDiagram
                    onLabelClickHandler={onLabelClickHandler}
                    names={['Rodion']}
                    multiple={false}
                    height={350}
                    data={data}
                />
            </Card>
        </Page>
    );
});

export default MainPage;
